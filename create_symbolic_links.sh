# !/bin/bash 
for file in $(pwd)/.config/*
	do
		ln -s ${file} $HOME/.config/
	done

ln -s $(pwd)/.vimrc $HOME/
ln -s $(pwd)/.gtkrc-2.0 $HOME/
ln -s $(pwd)/.imwheelrc $HOME/
ln -s $(pwd)/.xprofile $HOME/
ln -s $(pwd)/.zshenv $HOME/
ln -s $(pwd)/.zshrc $HOME/


