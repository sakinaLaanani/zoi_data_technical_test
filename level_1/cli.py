import click
from member_data_processor import Processor

@click.group()
def cli():
    pass

@click.command("process_log_files")
@click.option("-i", "--input_folder", help=" Input folder name")
@click.option("-o", "--output_folder", help="Output folder name")
def process_log_files(input_folder, output_folder):
    process_member_files = Processor(input_folder, output_folder)
    process_member_files.process_files()

cli.add_command(process_log_files)

if __name__ == "__main__":
    cli()