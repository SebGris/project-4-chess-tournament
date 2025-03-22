from jinja2 import Template
import webbrowser
import http.server
import socketserver


class PlayerReportGenerator:
    def __init__(self, players):
        self.players = players
        self.html_content = ""

    def generate_report(self):
        # Template HTML
        html_template = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Rapport des Tournois</title>
            <style>
                table { width: 100%; border-collapse: collapse; }
                th, td { border: 1px solid black; padding: 8px; text-align: left; }
                th { background-color: #f2f2f2; }
            </style>
        </head>
        <body>
            <h1>Liste de tous les joueurs par ordre alphabétique</h1>
                <table>
                    <tr>
                        <th>ID Joueur</th>
                        <th>Nom</th>
                        <th>Prénom</th>
                        <th>Date de naissance</th>
                        <th>ID échecs</th>
                    </tr>
                    {% for player in players %}
                        <tr>
                            <td>{{ player.id }}</td>
                            <td>{{ player.last_name }}</td>
                            <td>{{ player.first_name }}</td>
                            <td>{{ player.birth_date }}</td>
                            <td>{{ player.chess_id }}</td>
                        </tr>
                    {% endfor %}
                </table>
                <br>
        </body>
        </html>
        """
        # Générer le rapport HTML
        template = Template(html_template)
        self.html_content = template.render(players=self.players)

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
