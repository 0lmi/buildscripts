Source0: 2f587ae081d076e3707360c5db086520c219d3ea.tar.gz
%define srcdir lmdb-2f587ae081d076e3707360c5db086520c219d3ea/libraries/liblmdb
for i in %{_topdir}/SOURCES/00*.patch; do
    $PATCH -p3 < $i
done