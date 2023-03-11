import sys
import csv
import json
import praw
import yaml
import typer
from datetime import datetime

# noinspection PyUnresolvedReferences
import pretty_errors  # keep the import to have better error messages

from os.path import join
from pathlib import Path
from typer import Argument
from typer import Option
from typing import Optional, List
from loguru import logger #By default, loguru includes a timestamp, log level, module name, and line number in each log message, making it easy to trace the source of each message.
from codetiming import Timer
from pushshift_py import PushshiftAPI
from prawcore.exceptions import NotFound

class HelpMessages:
	Indicators = "Indicators code represent data that will be requested,Eg: To request the indicator GDP (Current US$), use its indicator code, NY.GDP.MKTP.CD"
	CountryCode = "3 letter ISO 3166-1 alpha-3 code, 2 letter ISO 3166-1 alpha-2 code, Eg: SEN for SENEGAL"
	Times = "Time can be a single year value or a range of years"
	Version = "Version identifiers are in the form YYYYMM, can be a range of version"
	output_dir = "Optional output directory"
	debug = "Enable debug logging"


# noinspection PyTypeChecker
@Timer(name="main", text="Total downloading time: {minutes:.1f}m", logger=logger.info)
def main(indicators: str = Argument(..., help=HelpMessages.Indicators),
		 countrycode: str = Option(..., help=HelpMessages.CountryCode),
		 times: List[int] = Option(..., help = HelpMessages.Times),
		 version: List[int] = Option(..., help = HelpMessages.Version),
		 output_dir: str = Option("./data/", help=HelpMessages.output_dir),
         debug: bool = Option(False, help=HelpMessages.debug) 

         ):

         logger.info('Testing the main arguments')
         logger.info(f'indicators {indicators}')
         logger.info(f'countrycode {countrycode}')
         logger.info(f'output_dir {output_dir}')





if __name__ == '__main__':
    typer.run(main)
