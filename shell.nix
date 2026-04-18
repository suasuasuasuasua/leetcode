{ self, pkgs, ... }:
let
  inherit (pkgs.stdenv.hostPlatform) system;
in
pkgs.mkShell.override { stdenv = pkgs.llvmPackages_21.stdenv; } {
  inherit (self.checks.${system}.git-hooks-check) shellHook;
  buildInputs = self.checks.${system}.git-hooks-check.enabledPackages;

  packages = with pkgs; [
    cmake
    cmake-language-server
    fmt
    git
    just
    llvmPackages_21.clang
    llvmPackages_21.clang-tools
    ninja
    python314
  ];
}
