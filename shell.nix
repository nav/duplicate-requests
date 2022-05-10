{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.poetry
    pkgs.python310
  ];

  shellHook = ''
    export PYTHONPATH=$(pwd)/src:$PYTHONPATH
  '';
}
