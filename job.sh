#!/bin/bash

if [ $# -gt 0 ]; then
    echo "Your command line contains $# arguments"
else
    echo "Your command line contains no arguments"
fi

arch=$1
pkg_name=$2
pkgtools_tag=$3
cmsdist_branch=$4
release_branch=$5
realease_queue=$6
echo $@ 
rm -rf pkgtools cmsdist	file.name
rm -rf build_pretend_cmssw_tool_conf 

git clone https://github.com/cms-sw/pkgtools -b $pkgtools_tag
git clone https://github.com/cms-sw/cmsdist -b $cmsdist_branch

./pkgtools/cmsBuild -i build_pretend_cmssw_tool_conf/ -c cmsdist/ --repository cms.week0 \
--arch $arch -j 16 --pretend build $pkg_name | tee logfile   


echo "Running python script to extract data"


rm -rf build_pretend_cmssw_tool_conf packet_write_wait: Connection to 188.184.104.86 port 22: Broken pipe
