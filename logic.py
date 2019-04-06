import requests
import multiprocessing as mp

# url = "http://challenges.laptophackingcoffee.org:8888/"

# img_source = "http://www.allthingsclipart.com/08/go.away.10.jpg"
#
# for dirr in range(0, 20):
#     if dirr < 10:
#         url = f"http://www.allthingsclipart.com/0{dirr}"
#     else:
#         url = f"http://www.allthingsclipart.com/{dirr}"
#     r = requests.get(url)
#     if r.status_code != 404:
#         print(f"directory: {dirr}; status_code: {r.status_code}")
#         # print(f"headers: {r.headers['content-type']}; encoding: {r.encoding}")
#         print(r.text)


# url = "http://www.allthingsclipart.com/08/go.away.10.jpg"
# r = requests.get(url)





def get_statuses(dirr):
    print(f"directory = {dirr}")
    if dirr < 10:
        url = f"http://www.allthingsclipart.com/0{dirr}"
    else:
        url = f"http://www.allthingsclipart.com/{dirr}"
    r = requests.get(url)
    return r.status_code
    # if r.status_code != 404:
    #     print(f"directory: {dirr}; status_code: {r.status_code}")
    #     # print(f"headers: {r.headers['content-type']}; encoding: {r.encoding}")
    #     print(r.text)


if __name__ == '__main__':
    num_processors = mp.cpu_count()

    print(f"Number of processors: {num_processors}")

    pool = mp.Pool(mp.cpu_count())
    results = pool.map(get_statuses, range(420))

    # Step 3: Don't forget to close
    pool.close()

    print(results)

