import shutil
from typing import Type

from pydantic import BaseModel, Field

from langchain.tools.file_management.utils import (
    INVALID_PATH_TEMPLATE,
    BaseFileTool,
    FileValidationError,
)


class FileCopyInput(BaseModel):
    """Input for CopyFileTool."""

    source_path: str = Field(..., description="Path of the file to copy")
    destination_path: str = Field(..., description="Path to save the copied file")

