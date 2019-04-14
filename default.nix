let
  pkgs = import <nixpkgs> {};
  stdenv = pkgs.stdenv;
in with pkgs; {
  myProject = stdenv.mkDerivation {
    name = "l33t-hax0r";
    version = "1";
    src = if pkgs.lib.inNixShell then null else nix;

    buildInputs =  [
      texlive.combined.scheme-full
    ];
  };
}
