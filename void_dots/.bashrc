# .bashrc

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias less='less --raw'
PS1='[\u@\h \W]\$ '
