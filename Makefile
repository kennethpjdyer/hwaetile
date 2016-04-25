
CALL = stow -vR
CONFIG = ~/.config
CALLCFG = $(CALL) -t $(CONFIG)
CALLHM = $(CALL) -t ~/

all: i3wmlink

i3wmlink:
	$(CALLCFG)/i3 i3



