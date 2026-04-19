{
  # Used to find the project root
  projectRootFile = "flake.nix";
  settings = {
    on-unmatched = "debug";
  };

  programs = {
    clang-format.enable = true;
    cmake-format.enable = true;
    isort.enable = true;
    nixfmt.enable = true;
    ruff.enable = true;
  };
}
