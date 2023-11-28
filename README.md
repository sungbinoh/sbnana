# Readme for myself...

## Environment setup

### New aliases

```
alias setup_sbnd='source /cvmfs/sbnd.opensciencegrid.org/products/sbnd/setup_sbnd.sh'
alias data_sbnd='cd /exp/sbnd/data/users/sungbino'
alias app_sbnd='cd /exp/sbnd/app/users/sungbino’
```

### Direcotry for test

In FNAL NFS
```
/exp/sbnd/app/users/sungbino/sbndana_test
```

### Build

```
$ ups list -aK+ sbnana
$ mrb newDev -v v09_78_06 -q e20:prof
$ source /exp/sbnd/app/users/sungbino/sbnana_test/localProducts_larsoft_v09_78_06_e20_prof/setup
$ cd srcs
$ mrb gitCheckout sbnana
$ cd sbnana
$ git tag
$ git checkout v09_78_06
$ git checkout -b v09_78_06
$ cd ../
$ mrbsetenv
$ mrb install -j4
```

### Added setup.sh file in the main direcoty

Content of the setup.sh

```
source /cvmfs/sbnd.opensciencegrid.org/products/sbnd/setup_sbnd.sh
source /exp/sbnd/app/users/sungbino/sbnana_test/localProducts_larsoft_v09_78_06_e20_prof/setup
mrbsetenv
setup sam_web_client
```
