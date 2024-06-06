import os
import datetime
import git


def main():
    # 設定專案目錄
    #repo_dir = '/path/to/your/repository'
    repo_dir = 'C:\Users\yuyu\Desktop\githubRepo\leetcodeMedium'
    repo = git.Repo(repo_dir)

    # 確認是否有變更
    if repo.is_dirty(untracked_files=True):
        # 添加所有變更
        repo.git.add(A=True)

        # 提交變更
        commit_message = f"Daily automated commit on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        repo.index.commit(commit_message)

        # 推送變更
        origin = repo.remote(name='origin')
        origin.push()

if __name__ == "__main__":
    main()
