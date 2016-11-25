1. copy {Dir}/resources/vcap_np to  cd /var/vcap/packages/cflinuxfs2/rootfs/etc/sudoers.d/ in all diego_cells.
2. chmod 440 vcap_np.
3. run ./package.sh to package the jexus_buildpack_offline.zip. should execute on linux os.
