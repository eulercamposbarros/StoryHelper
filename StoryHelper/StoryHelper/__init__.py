"""
Package for StoryHelper.
"""
import dotenv, os, django

dotenv.read_dotenv()
os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "StoryHelper.settings")
