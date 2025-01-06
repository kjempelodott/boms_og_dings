# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=10000
SAVEHIST=10000

setopt autocd extendedglob
unsetopt beep
bindkey -e

bindkey "^[[1~" beginning-of-line
bindkey "^[[3~" delete-char
bindkey "^[[4~" end-of-line
bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word
bindkey -s "^[[5~" ""
bindkey -s "^[[6~" ""

# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/lodott/.zshrc'

autoload -Uz compinit
compinit

md() {
    if [ -z "$1" ]
    then
        echo "No input file provided"
    else
        pandoc -thtml < "$1" | elinks -dump -dump-color-mode 2 | less -R
    fi
}

PROMPT=$'%F{red}%m %f| '
RPROMPT=$'%F{blue}%~'

source $HOME/.aliases
