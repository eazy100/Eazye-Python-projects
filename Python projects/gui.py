# Ensure the 'rich' library is installed
# pip install rich

import calendar
from rich.console import Console
from rich.table import Table

def colorful_calendar(year):
    console = Console()
    months = [calendar.month_calendar(year, m) for m in range(1, 13)]
    for month in range(12):
        month_name = calendar.month_name[month + 1]
        cal_str = calendar.TextCalendar().formatmonth(year, month + 1)
        print(cal_str)
        print(f"\n{month_name} {year}\n")
        # Create a table for each month
        table = Table(title=f"[bold cyan] {month_name} \
                {year} [/bold cyan]", box=None, show_header=True, header_style="bold magenta")
        table = Table(title=f"[bold cyan] {month_name}"
                f" {year} [/bold cyan]", box=None, show_header=True, header_style="bold magenta")
        # Add the headers for the days of the week 
        table.add_column("Sun", style="blue")
        table.add_column("Mon", style="blue")
        table.add_column("Tue", style="blue")
        table.add_column("Wed", style="blue")
        table.add_column("Thu", style="blue")
        table.add_column("Fri", style="blue")
        table.add_column("Sat", style="blue")

        # Add the days to the table
        for week in months[month]:
            table.add_row(*[f"{day:2}" if day != 0 else "" for day in week])

        # Print the table
        console.print(table)

    # Add headers
    table.add_column("Sun", style="red")
    table.add_column("Mon", style="yellow")
    table.add_column("Tue", style="green")
    table.add_column("Wed", style="blue")
    table.add_column("Thu", style="magenta")
    table.add_column("Fri", style="cyan")
    table.add_column("Sat", style="white")

    # Split the calendar string into weeks
    weeks = cal_str.split('\n')[2:-1]  # Skip the first two lines (header and empty line) and last line (empty line)
    
    for week in weeks:
        days = week.split()
        table.add_row(*days)

    console.print(table)
    console.print(f"\n[bold green]Happy {year}[/bold green]") 
    colorful_calendar(2025)