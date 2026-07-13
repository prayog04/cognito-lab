"""Entry point for the trading agent."""

from __future__ import annotations

from src.trading_routine.agent import create_client


def main() -> None:
    client = create_client()
    print("Trading agent ready.")


if __name__ == "__main__":
    main()
