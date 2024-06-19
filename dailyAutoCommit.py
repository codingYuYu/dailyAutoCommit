import os
import subprocess
import datetime
import git


def main():
    # 設定專案目錄
    #repo_dir = '/path/to/your/repository'
    repo_dir = r'C:\Users\yuyu\Desktop\githubRepo\autoCommitTest'

    # 將當前工作目錄更改為repo_dir
    os.chdir(repo_dir)



    repo = git.Repo(repo_dir)

    # 確認是否有變更
    #if repo.is_dirty(untracked_files=True):
    # 添加所有變更
    repo.git.add(A=True)

    # 提交變更
    commit_message = f"Daily automated commit on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    print(commit_message)
    repo.index.commit(commit_message)


    # 使用 git push -uf origin main 進行推送
    #os.system('git push -uf origin main')

    # 使用個人訪問令牌進行身份驗證
    # github_token = os.getenv('GITHUB_TOKEN')  # 從環境變量中獲取個人訪問令牌
    # os.system('git push -uf origin main')
    #github_token = os.getenv('GITHUB_TOKEN')  # 從環境變量中獲取個人訪問令牌
    #os.system(f'git push -uf https://{github_token}@github.com/codingYuYu/leetcodeMedium.git main')
    # 使用SSH URL進行推送
    github_ssh_url = "git@github.com:codingYuYu/autoCommitTest.git"

    # 使用 git push -uf origin main 進行推送
    os.system(f'git push -uf {github_ssh_url} main')


if __name__ == "__main__":
    main()
