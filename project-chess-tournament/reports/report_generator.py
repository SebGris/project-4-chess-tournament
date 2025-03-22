from jinja2 import Template
import webbrowser
import http.server
import socketserver


class ReportGenerator:
    def __init__(self):
        self.html_content = ""

    def generate_report_and_serve(
        self, data, template_title, table_headers, row_template
    ):
        # Template HTML
        html_template = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{template_title}</title>
            <style>
                table {{ width: 100%; border-collapse: collapse; }}
                th, td {{ border: 1px solid black; padding: 8px; text-align: left; }}
                th {{ background-color: #f2f2f2; }}
            </style>
        </head>
        <body>
            <h1>{template_title}</h1>
            <table>
                <tr>
                    {''.join(f'<th>{header}</th>' for header in table_headers)}
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
        # Générer le rapport HTML
        template = Template(html_template)
        self.html_content = template.render(data=data)
        self.serve_report()

    def generate_players_report(self, players):
        headers = [
            "N° ID du Joueur",
            "Nom",
            "Prénom",
            "Date de naissance",
            "ID échecs"
        ]
        row_template = """
            <td>{{ item.id }}</td>
            <td>{{ item.last_name }}</td>
            <td>{{ item.first_name }}</td>
            <td>{{ item.birth_date }}</td>
            <td>{{ item.chess_id }}</td>
        """
        self.generate_report_and_serve(
            players,
            "Liste de tous les joueurs par ordre alphabétique",
            headers,
            row_template
        )

    def generate_tournaments_report(self, tournaments):
        headers = [
            "N° ID du Tournoi",
            "Nom",
            "Emplacement",
            "Date de début",
            "Date de fin",
            "Nombre de round"
        ]
        row_template = """
            <td>{{ item.id }}</td>
            <td>{{ item.name }}</td>
            <td>{{ item.location }}</td>
            <td>{{ item.start_date }}</td>
            <td>{{ item.end_date }}</td>
            <td>{{ item.total_rounds }}</td>
        """
        self.generate_report_and_serve(
            tournaments,
            "Liste de tous les tournois",
            headers,
            row_template
        )

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
