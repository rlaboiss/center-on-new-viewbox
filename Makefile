DESTDIR = $(HOME)/.config/inkscape/extensions
NAME = set-a4-viewport

.PHONY: install
install:
	install $(NAME).py $(DESTDIR)
	install --mode=644 $(NAME).inx $(DESTDIR)

.PHONY: uninstall
uninstall:
	rm -f $(DESTDIR)/$(NAME).*

.PHONY: lint
lint:
	for i in isort flake8 black pylint ; do $$i *.py ; done
