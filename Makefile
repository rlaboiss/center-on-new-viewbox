DESTDIR = $(HOME)/.config/inkscape/extensions
NAME = center-on-new-viewbox

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
