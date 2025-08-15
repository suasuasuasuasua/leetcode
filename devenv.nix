{ pkgs, ... }:
{
  # https://devenv.sh/packages/
  packages = with pkgs; [
    git
    nil
    python313Packages.ipython
    python313Packages.python-lsp-server
  ];

  # https://devenv.sh/languages/
  languages.python = {
    enable = true;
    version = "3.13";
  };

  # https://devenv.sh/git-hooks/
  git-hooks.hooks = {
    black.enable = true;
    isort.enable = true;
    nixfmt-rfc-style.enable = true;
  };

  # See full reference at https://devenv.sh/reference/options/
}
