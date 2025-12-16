import os
import glob

import argostranslate.package


def main() -> None:
  """
  Install all .argosmodel files found in the local 'models' directory
  into the Argos Translate packages directory used by LibreTranslate.
  """
  base_dir = os.path.dirname(os.path.abspath(__file__))
  models_dir = os.path.join(base_dir, "models")

  if not os.path.isdir(models_dir):
    print(f"'models' directory not found at: {models_dir}")
    return

  model_paths = glob.glob(os.path.join(models_dir, "*.argosmodel"))

  if not model_paths:
    print(f"No .argosmodel files found in: {models_dir}")
    return

  print("Installing Argos models from:", models_dir)
  for path in model_paths:
    print("  Installing model:", os.path.basename(path))
    try:
      argostranslate.package.install_from_path(path)
    except Exception as exc:  # noqa: BLE001
      print("    Failed to install", path, "->", exc)

  print("Done installing models.")


if __name__ == "__main__":
  main()


