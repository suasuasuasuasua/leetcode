{ pkgs, ... }:
{
  # Used to find the project root
  projectRootFile = "flake.nix";
  settings = {
    on-unmatched = "debug";
  };

  programs = {
    cmake-format.enable = true;
    clang-format.enable = true;
    nixfmt.enable = pkgs.lib.meta.availableOn pkgs.stdenv.buildPlatform pkgs.nixfmt-rfc-style.compiler;
    nixfmt.package = pkgs.nixfmt-rfc-style;
    ruff.enable = true;
  };
}
