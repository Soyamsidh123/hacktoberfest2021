import threading
from datetime import datetime

# Player Management System
class Player:
    def __init__(self, player_id, name, position):
        self.player_id = player_id
        self.name = name
        self.position = position
        self.statistics = {}

    def update_statistics(self, stat_name, value):
        self.statistics[stat_name] = value

    def get_statistics(self):
        return self.statistics

# Match Schedule Management
class Schedule:
    def __init__(self):
        self.matches = []

    def add_match(self, date, team1, team2):
        self.matches.append({'date': date, 'team1': team1, 'team2': team2})

    def get_matches(self):
        return self.matches

# Ticket Booking System
class Ticket:
    def __init__(self, ticket_id, match):
        self.ticket_id = ticket_id
        self.match = match
        self.is_booked = False

    def book_ticket(self):
        if not self.is_booked:
            self.is_booked = True
            return True
        return False

    def cancel_ticket(self):
        if self.is_booked:
            self.is_booked = False
            return True
        return False

# Team Management System
class Team:
    def __init__(self, team_id, name):
        self.team_id = team_id
        self.name = name
        self.roster = []

    def add_player(self, player):
        self.roster.append(player)

    def get_roster(self):
        return self.roster

# Booking Management System
class Booking:
    def __init__(self):
        self.bookings = {}

    def book_ticket(self, ticket):
        if ticket.book_ticket():
            self.bookings[ticket.ticket_id] = ticket
            return True
        return False

    def cancel_ticket(self, ticket):
        if ticket.cancel_ticket():
            del self.bookings[ticket.ticket_id]
            return True
        return False

# Multi-Threaded Report Generation
class MLBBackend:
    def __init__(self):
        self.players = []
        self.schedule = Schedule()
        self.tickets = Booking()

    def add_player(self, player):
        self.players.append(player)

    def generate_report(self):
        report = "Player Statistics Report\n"
        report += "-" * 30 + "\n"
        for player in self.players:
            report += f"Player: {player.name}, ID: {player.player_id}, Stats: {player.get_statistics()}\n"
        print(report)

    def start_report_generation(self):
        report_thread = threading.Thread(target=self.generate_report)
        report_thread.start()
        report_thread.join()

# Main method to demonstrate functionality
def main():
    # Create MLB Backend
    mlb_backend = MLBBackend()

    while True:
        print("\n--- MLB Digital Platform Management ---")
        print("1. Add Player")
        print("2. Add Match")
        print("3. Book Ticket")
        print("4. Generate Report")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            player_id = input("Enter Player ID: ")
            name = input("Enter Player Name: ")
            position = input("Enter Player Position: ")
            player = Player(player_id, name, position)
            mlb_backend.add_player(player)

            # Option to update statistics
            stat_name = input("Do you want to update statistics for this player? (yes/no): ")
            if stat_name.lower() == 'yes':
                while True:
                    stat_name = input("Enter Statistic Name (or 'done' to finish): ")
                    if stat_name.lower() == 'done':
                        break
                    value = input(f"Enter value for {stat_name}: ")
                    player.update_statistics(stat_name, value)
            print(f"Player {name} added successfully!")

        elif choice == '2':
            date_str = input("Enter Match Date (YYYY-MM-DD): ")
            date = datetime.strptime(date_str, '%Y-%m-%d')
            team1 = input("Enter Team 1 Name: ")
            team2 = input("Enter Team 2 Name: ")
            mlb_backend.schedule.add_match(date, team1, team2)
            print(f"Match scheduled between {team1} and {team2} on {date_str}.")

        elif choice == '3':
            match_id = int(input("Enter Match ID (starting from 0): "))
            if match_id < len(mlb_backend.schedule.get_matches()):
                match = mlb_backend.schedule.get_matches()[match_id]
                ticket_id = input("Enter Ticket ID: ")
                ticket = Ticket(ticket_id, match)
                if mlb_backend.tickets.book_ticket(ticket):
                    print(f"Ticket {ticket_id} booked successfully for {match['team1']} vs {match['team2']}.")
                else:
                    print("Ticket booking failed.")
            else:
                print("Invalid Match ID.")

        elif choice == '4':
            mlb_backend.start_report_generation()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
