from jinja2 import Template

# Exemple de données
tournaments = [
    {
        "tournament_id": 1,
        "name": "Tournoi de Printemps",
        "players": [
            {"player_id": 101, "name": "John Doe", "score": 50},
            {"player_id": 102, "name": "Jane Smith", "score": 60},
        ]
    },
    {
        "tournament_id": 2,
        "name": "Tournoi d'Été",
        "players": [
            {"player_id": 103, "name": "Alice Johnson", "score": 70},
            {"player_id": 104, "name": "Bob Brown", "score": 80},
        ]
    }
]

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
    <h1>Rapport des Tournois</h1>
    {% for tournament in tournaments %}
        <h2>{{ tournament.name }}</h2>
        <table>
            <tr>
                <th>ID Joueur</th>
                <th>Nom</th>
                <th>Score</th>
            </tr>
            {% for player in tournament.players %}
                <tr>
                    <td>{{ player.player_id }}</td>
                    <td>{{ player.name }}</td>
                    <td>{{ player.score }}</td>
                </tr>
            {% endfor %}
        </table>
        <br>
    {% endfor %}
</body>
</html>
"""

# Générer le rapport HTML
template = Template(html_template)
html_output = template.render(tournaments=tournaments)

# Sauvegarder le rapport dans un fichier HTML
with open("tournament_report.html", "w") as file:
    file.write(html_output)

print("Rapport généré avec succès : tournament_report.html")
