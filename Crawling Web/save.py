import csv

def save_to_file(jobs):
  #file 여는 변수 저장
  file = open("jobs.csv",mode="w")
  # wrtier로 파일에 csv 작성
  writer = csv.writer(file)
  writer.writerow(["title", "company", "loaction", "link"])
  for job in jobs:
    #dictionary 사용
    writer.writerow(list(job.values()))
  print(jobs)
  return 