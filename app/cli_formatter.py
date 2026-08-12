from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.rule import Rule
from rich.text import Text


console = Console()


def print_pipeline_start(topic: str) -> None:
    console.print()
    console.print(
        Panel(
            f"[bold white]{topic}[/bold white]",
            title="[bold green]🔬 Research Pipeline[/bold green]",
            subtitle="Agentic AI Research System",
            border_style="green",
            padding=(1, 2),
        )
    )


def print_step(number: int, title: str) -> None:
    console.print()
    console.print(
        Rule(
            f"[bold blue]Step {number} • {title}[/bold blue]",
            style="blue",
        )
    )


def print_search_results(content: str) -> None:
    console.print(
        Panel(
            Markdown(content),
            title="[bold cyan]🔎 Search Results[/bold cyan]",
            border_style="cyan",
            padding=(1, 2),
        )
    )


def print_scraped_content(content: str) -> None:
    console.print(
        Panel(
            Markdown(content),
            title="[bold yellow]🌐 Scraped Content[/bold yellow]",
            border_style="yellow",
            padding=(1, 2),
        )
    )


def print_research_report(content: str) -> None:
    console.print(
        Panel(
            Markdown(content),
            title="[bold magenta]📝 Research Report[/bold magenta]",
            border_style="magenta",
            padding=(1, 2),
        )
    )


def print_critique(content: str) -> None:
    console.print(
        Panel(
            Markdown(content),
            title="[bold red]🧠 Critique[/bold red]",
            border_style="red",
            padding=(1, 2),
        )
    )


def print_success(message: str) -> None:
    console.print(
        Panel(
            Text(message, style="bold green"),
            border_style="green",
            padding=(0, 2),
        )
    )


def print_error(message: str) -> None:
    console.print(
        Panel(
            Text(message, style="bold red"),
            title="[bold red]Error[/bold red]",
            border_style="red",
            padding=(0, 2),
        )
    )