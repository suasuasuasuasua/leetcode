{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.11";
    git-hooks.url = "github:cachix/git-hooks.nix";
    treefmt-nix.url = "github:numtide/treefmt-nix";
  };

  outputs =
    {
      self,
      nixpkgs,
      git-hooks,
      treefmt-nix,
      ...
    }:
    let
      supportedSystems = [
        "x86_64-linux"
        "x86_64-darwin"
        "aarch64-linux"
        "aarch64-darwin"
      ];
      forEachSystem = f: nixpkgs.lib.genAttrs supportedSystems (system: f pkgsFor.${system});
      pkgsFor = nixpkgs.lib.genAttrs supportedSystems (system: nixpkgs.legacyPackages.${system});

      # Eval the treefmt modules from ./treefmt.nix
      treefmtEval = forEachSystem (pkgs: treefmt-nix.lib.evalModule pkgs ./treefmt.nix);
    in
    {
      #  for `nix fmt`
      formatter = forEachSystem (
        pkgs: treefmtEval.${pkgs.stdenv.hostPlatform.system}.config.build.wrapper
      );

      devShells = forEachSystem (pkgs: {
        default = import ./shell.nix {
          inherit pkgs self;
        };
      });

      checks = forEachSystem (pkgs: {
        formatting = treefmtEval.${pkgs.stdenv.hostPlatform.system}.config.build.check self;
        git-hooks-check = git-hooks.lib.${pkgs.stdenv.hostPlatform.system}.run {
          src = ./.;
          imports = [ ./git-hooks.nix ];
        };
      });
    };
}
