""" Collects commit data for contributors of the master branch of a repo. """
from pydriller import RepositoryMining

repo = "https://github.com/lussierc/simplePerformanceExperimentsJava"

def collect_commits_hash(repo):
    """
    Creates a list of dictionaries that contains commit info.

    hash (str): hash of the commit
    msg (str): commit message
    author_name (str): commit author name
    author_email (str): commit author email
    author_date (datetime): authored date
    merge (Bool): True if the commit is a merge commit
    added: number of lines added
    removed: number of lines removed
    nloc: Lines Of Code (LOC) of the file
    complexity: Cyclomatic Complexity of the file
    methods: list of methods of the file.
    filename: files modified by commit.
    """

    commit_list = []

    for commit in RepositoryMining(repo).traverse_commits():

        line_added = 0
        line_removed = 0
        line_of_code = 0
        complexity = 0
        methods = []
        filename = []
        filepath = []

        for item in commit.modifications:
            # modifications is a list of files and its changes
            line_added += item.added
            line_removed += item.removed
            if item.nloc is not None:
                line_of_code += item.nloc
            if item.complexity is not None:
                complexity += item.complexity

            for method in item.methods:
                methods.append(method.name)
            filename.append(item.filename)
            filepath.append(item.new_path)


        single_commit_dict = {
            "hash": commit.hash,
            "author_msg": commit.msg,
            "author_name": commit.author.name,
            "author_email": commit.author.email,
            "author_date": commit.author_date.date(),
            "merge": commit.merge,
            "line_added": line_added,
            "line_removed": line_removed,
            "lines_of_code": line_of_code,
            "complexity": complexity,
            "methods": methods,
            "filename": filename,
            "filepath": filepath,
        }

        commit_list.append(single_commit_dict)

    print(commit_list)
collect_commits_hash(repo)
