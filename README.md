# xKAN-meta_testing
* `.github/workflows/build-push-image.yml` is used to build new Docker images using `Dockerfile` on push to master.
* `action.yml` is the definition of the GitHub Action, it tells workflows using this action to pull and run the `ksp-ckan/metadata-ci` image.
* The container will install some dependencies and then run `NetKAN/build.sh`.

* This action can be used by putting `NetKAN/ckan-metadata-ci.yml` into the directory `.github/workflows/` of your repository.

# Limitations
Currently only runs the `build.sh` for .netkan files.


# TODO
* Replace both `build.sh`:
  * by a Python rewrite
  * that can handle .ckan and .netkan files in one go
  * that makes less assumptions about the environment, like target branch (->`github.base_ref`), or the location of the .netkan files (create input?)
  * that caches mod downloads in a ways that doesn't overflow the available cache storage



Contributions
=============

These were moved over from KSP-CKAN/CKAN-meta and KSP-CKAN/NetKAN. Thanks
to all the contributions from the following in no particular order.

Matthew Heguy
Leon Wright
Dwayne Bent
Willhelm Rendahl
Paul Fenwick
Alexander Dzhoganov
Magnus Aagaard Sørensen
Hakan Tandogan
Myk Dowling
Arne Peirs
