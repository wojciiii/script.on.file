all:
	@echo "Creating repository."
	python2 _tools/generate_repo.py

clean:
	@rm -f context.on.file.zip
	@rm -f script.on.file.zip
	@rm -fr wojci.home
	@rm -fr _repository-install
