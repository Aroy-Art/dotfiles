################################
#--------- Text Editor --------#
export EDITOR=/usr/bin/nano
################################

################################
#----------- Browser ----------#
if [ -r "$HOME/.zprofile" ] ; then
    export BROWSER=/usr/bin/vivaldi-stable       
fi
################################

################################
#------------ NPM -------------#
PATH="$HOME/.local/bin:$PATH"
export npm_config_prefix="$HOME/.local"
################################

################################
#------- ADB - Fastboot -------#
if [ -d "$HOME/.adb-fastboot/platform-tools" ] ; then
    export PATH="$HOME/.adb-fastboot/platform-tools:$PATH"
fi
################################

################################
#---------- RubyGems ----------#
export GEM_HOME="$(ruby -e 'puts Gem.user_dir')"
export PATH="$PATH:$GEM_HOME/bin"
################################
