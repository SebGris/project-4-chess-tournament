import http.server
import socketserver
import webbrowser
from jinja2 import Template


class ReportGenerator:
    def __init__(self):
        self.html_content = ""

    def generate_html_report(self, html_template, data):
        template = Template(html_template)
        self.html_content = template.render(data=data)
        self.serve_report()

    def __create_html_template(self, title_h1, headers, fields, title_h2=""):
        row_template = ''.join(
            f"<td>{{{{ item.{field} }}}}</td>" for field in fields
        )
        return f"""
        <!DOCTYPE html>
        <html lang="en">
        {self.__create_head_html(title_h1)}
            <h1>{title_h1}</h1>
            {f"<h2>{title_h2}</h2>" if title_h2 else ""}
            <table>
                <tr>
                    {''.join(f'<th>{header}</th>' for header in headers)}
                </tr>
                {{% for item in data %}}
                    <tr>
                        {row_template}
                    </tr>
                {{% endfor %}}
            </table>
            <br>
        </body>
        </html>
        """

    def __create_head_html(self, title):
        return f"""
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, "
                  "initial-scale=1.0">
            <title>{title}</title>
            <style>
                table {{ width: 100%; border-collapse: collapse; }}
                th, td {{
                    border: 1px solid black;
                    padding: 8px;
                    text-align: left;
                }}
                th {{ background-color: #f2f2f2; }}
            </style>
        </head>
        <body>
        """

    def generate_players_report(self, players):
        html_template = self.__create_html_template(
            "Liste de tous les joueurs par ordre alphabétique",
            [
                "N° du Joueur", "Nom", "Prénom",
                "Date de naissance", "ID échecs"
            ],
            ["id", "last_name", "first_name", "birth_date", "chess_id"]
        )
        self.generate_html_report(html_template, players)

    def generate_tournaments_report(self, tournaments):
        html_template = self.__create_html_template(
            "Liste de tous les tournois",
            [
                "N° du Tournoi", "Nom", "Emplacement",
                "Date de début", "Date de fin", "Nombre de round"
            ],
            [
                "id", "name", "location",
                "start_date", "end_date", "total_rounds"
            ]
        )
        self.generate_html_report(html_template, tournaments)

    def generate_tournament_name_and_dates_report(self, tournament):
        html_template = self.__create_html_template(
            "Nom et dates du tournoi",
            ["Nom", "Date de début", "Date de fin"],
            ["name", "start_date", "end_date"]
        )
        self.generate_html_report(html_template, [tournament])

    def generate_tournament_players_report(self, players, title):
        html_template = self.__create_html_template(
            "Liste des joueurs du tournoi",
            [
                "N° du Joueur", "Nom", "Prénom",
                "Date de naissance", "ID échecs"
            ],
            ["id", "last_name", "first_name", "birth_date", "chess_id"],
            title
        )
        self.generate_html_report(html_template, players)

    def generate_rounds_matches_report(self, rounds):
        title = "Liste des tours du tournoi et de tous les matchs"
        html_template = f"""
        <!DOCTYPE html>
        <html lang="en">
        {self.__create_head_html(title)}
        <body>
            <h1>Liste des tours du tournoi et de tous les matchs</h1>
            {{% for round in data %}}
                <h2>Nom du tour : {{{{ round.name }}}}</h2>
                <table>
                    <tr>
                        <th>Match</th>
                        <th>Joueur 1</th>
                        <th>Score</th>
                        <th>Joueur 2</th>
                        <th>Score</th>
                    </tr>
                    {{% for match in round.matches %}}
                        <tr>
                            <td>{{{{ match.index }}}}</td>
                            <td>{{{{ match.player1 }}}}</td>
                            <td>{{{{ match.player1_score }}}}</td>
                            <td>{{{{ match.player2 }}}}</td>
                            <td>{{{{ match.player2_score }}}}</td>
                        </tr>
                    {{% endfor %}}
                </table>
                <br>
            {{% endfor %}}
        </body>
        </html>
        """
        self.generate_html_report(html_template, rounds)

    def serve_report(self):
        # Serveur HTTP temporaire pour afficher le rapport
        def create_request_handler(report_content):
            class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):
                def do_GET(self):
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(report_content.encode('utf-8'))
            return CustomRequestHandler

        PORT = 8000
        handler = create_request_handler(self.html_content)

        with socketserver.TCPServer(("", PORT), handler) as httpd:
            print(f"Serving report at http://localhost:{PORT}")
            webbrowser.open(f"http://localhost:{PORT}")
            httpd.handle_request()  # Serve one request
            httpd.server_close()
