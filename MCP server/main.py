# server.py
from mcp.server.fastmcp import FastMCP
import os
# Create an MCP server
mcp = FastMCP("sticky notes")

notes_file = os.path.join(os.path.dirname(__file__), "notes.txt")
# This is the file where we will store the notes

def ensure_file_exists():
    if not os.path.exists(notes_file):
        with open(notes_file, 'w') as f: #w mode so we can overridden            f.write("")
            f.write("")
@mcp.tool()
def add_note(note: str) -> str:
    """
    Add a note to the notes file.
    
    Args:
        note (str): The note to add.
    Returns:
        str: A message indicating the note was added.
    """ 
    # the above is a docstring, it is used to generate the help message
    # and is not executed

    ensure_file_exists()
    with open(notes_file, 'a') as f: #a mode to append
        f.write(note + "\n")
    return f"Note added: {note}"

@mcp.tool()
def list_notes() -> str:
    """
    List all notes in the notes file.
    
    Returns:
        str: The notes in the file.
    """
    ensure_file_exists()
    with open(notes_file, 'r') as f:
        content = f.read().strip()
    return content or "No notes found."

@mcp.resource("notes://latest")
def get_latest_note() -> str:
    """
    Get the latest note from the notes file.
    
    Returns:
        str: The latest note.
    """
    ensure_file_exists()
    with open(notes_file, 'r') as f:
        lines = f.readlines()
    return lines[-1].strip() if lines else "No notes found."


@mcp.prompt()
def prompt_for_note() -> str:
    """
    Prompt the user for a note.
    
    Returns:x
        str: The note entered by the user.
    """
    ensure_file_exists()
    with open(notes_file, 'r') as f:
        content = f.read().strip()
    if not content:
        return "No notes found."
    return f"summa {content}"