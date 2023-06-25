# _*_ coding: utf-8 _*_
# @Time: 2023/5/20 16:21
# @Author: 🎈
# @File: demo1

import asyncio
import time
import aiohttp


async def req(i):
    urls = [
        'https://i2.wp.com/lh3.ggpht.com/-RPXwANAI3qo/Yxy9OOTjkzI/AAAAAAABh70/m3KmiHWHkQUtC5AAsCckcRdDxpqYFELuACNcBGAsYHQ/s0-rw/cosplay-byoru-yamato-4khd.com-0042-0015.jpg',
        'https://i2.wp.com/lh3.ggpht.com/-dolmLTTX3LE/Yxy9KDYSZQI/AAAAAAABh7U/5PLyeQv5rBIadBY-5bu932uABn1VJ37dgCNcBGAsYHQ/s0-rw/cosplay-byoru-yamato-4khd.com-0020-007.jpg',
        'https://i2.wp.com/lh3.ggpht.com/-EDDdjplJ_Ls/Yxy9MHEi85I/AAAAAAABh7k/71CE7Su36KMn1N6TgryqllSArpuLDkCGwCNcBGAsYHQ/s0-rw/cosplay-byoru-yamato-4khd.com-0030-0011.jpg',
        'https://i2.wp.com/lh3.ggpht.com/-qfn4RNt5wNA/Yxy9O13AAWI/AAAAAAABh78/amubQQti7egP8dH5-gcQNYgR99K4yFiewCNcBGAsYHQ/s0-rw/cosplay-byoru-yamato-4khd.com-0049-0017.jpg',
        'https://i2.wp.com/lh3.ggpht.com/-v_RVgJw1XlA/Yxy9LfSePtI/AAAAAAABh7g/HMB8fKYKAYwCpIwHOhtne9v8kszydVlEACNcBGAsYHQ/s0-rw/cosplay-byoru-yamato-4khd.com-0027-0010.jpg',
        'https://i2.wp.com/lh3.ggpht.com/-QGdCSWVs1dA/Yxy9LFimZfI/AAAAAAABh7c/FmCZZwBDGx0XsRslntGtftQdcGHb4LzVwCNcBGAsYHQ/s0-rw/cosplay-byoru-yamato-4khd.com-0026-009.jpg',
        'https://i2.wp.com/lh3.ggpht.com/-uIkagiVbAFA/Yxy9NhEMjRI/AAAAAAABh7w/Sq3jPWW-r4ctHg29gF5MEk1AKlgUrw4lgCNcBGAsYHQ/s0-rw/cosplay-byoru-yamato-4khd.com-0039-0014.jpg',
        'https://i2.wp.com/lh3.ggpht.com/-8JJSwuvQHng/Yxy9Mon-UPI/AAAAAAABh7o/tj-upDpHbR8NLlqfdTe3CqrP1dp3UehiACNcBGAsYHQ/s0-rw/cosplay-byoru-yamato-4khd.com-0033-0012.jpg',
        'https://i2.wp.com/lh3.ggpht.com/-F5udOgcWsNE/Yxy9M2Iz5XI/AAAAAAABh7s/SrvvLsC02iovgNSGja_bOXzMnOhKksaIwCNcBGAsYHQ/s0-rw/cosplay-byoru-yamato-4khd.com-0036-0013.jpg',
        'https://i2.wp.com/lh3.ggpht.com/-VLktO7BRFtA/Yxy9IqcWv-I/AAAAAAABh7I/IZP3NU457vcB1Sc_7r1zYjb5L8SYIKSegCNcBGAsYHQ/s0-rw/cosplay-byoru-yamato-4khd.com-0012-004.jpg',
        'https://i2.wp.com/lh3.ggpht.com/-Ktp63T3bPqM/Yxy9QlNoIbI/AAAAAAABh8I/lkep_5MhmD8zUDsmE6b9b8A6a9TFwIOCACNcBGAsYHQ/s0-rw/cosplay-byoru-yamato-4khd.com-0058-0020.jpg',
        'https://i2.wp.com/lh3.ggpht.com/-DBgqpLr24g8/Yxy9I0BS-DI/AAAAAAABh7M/lPwZ56hTdAk1QM1lfXZ632fqJnHJjbU3ACNcBGAsYHQ/s0-rw/cosplay-byoru-yamato-4khd.com-0015-005.jpg',
        'https://i2.wp.com/lh3.ggpht.com/-3NFk3-ZX4lk/Yxy9JSMyKeI/AAAAAAABh7Q/DvixVufmz_MFHzy52j_3fip6LppSSRUkgCNcBGAsYHQ/s0-rw/cosplay-byoru-yamato-4khd.com-0017-006.jpg',
        'https://i2.wp.com/lh3.ggpht.com/-XeXkfDD755w/Yxy9PzshCzI/AAAAAAABh8E/js_wyQaCDsQO_TWX_n0UP6o0U1XU9FCsQCNcBGAsYHQ/s0-rw/cosplay-byoru-yamato-4khd.com-0054-0019.jpg',
        'https://i2.wp.com/lh3.ggpht.com/-SINthkDH2jo/Yxy9Pno3FpI/AAAAAAABh8A/Z6f8hc48GmIprPdesiiPUWeN3bhTnx-0QCNcBGAsYHQ/s0-rw/cosplay-byoru-yamato-4khd.com-0052-0018.jpg',
        'https://i2.wp.com/lh3.ggpht.com/-46H_lJtrViE/Yxy9HmxztdI/AAAAAAABh7E/JukuHFnJzfo2YBJM3N7QQQWMgqYkYJVBwCNcBGAsYHQ/s0-rw/cosplay-byoru-yamato-4khd.com-0003-001.jpg',
        'https://i2.wp.com/lh3.ggpht.com/-KmZdGTHjhT4/Yxy9HgfPhfI/AAAAAAABh7A/6KZfmE91gnAfPp4Dtm1mJAjajjMKtH91wCNcBGAsYHQ/s0-rw/cosplay-byoru-yamato-4khd.com-0009-003.jpg',
        'https://i2.wp.com/lh3.ggpht.com/-p1cwZE1hJjo/Yxy9Hnqe5AI/AAAAAAABh68/4l0N_UYj_pwJEsLxF59lqLr8YrImPv6UACNcBGAsYHQ/s0-rw/cosplay-byoru-yamato-4khd.com-0006-002.jpg',
        'https://i2.wp.com/lh3.ggpht.com/-Fsb9tOqj898/Yxy9Kp0W3fI/AAAAAAABh7Y/KJqbTnc7hXQjfdcHpHynV2kMZHJl_L2BACNcBGAsYHQ/s0-rw/cosplay-byoru-yamato-4khd.com-0023-008.jpg',
    ]
    print(f'正在读...{i}')
    await asyncio.sleep(1)


async def main():
    tasks = [asyncio.create_task(test(i)) for i in range(100)]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    s = time.time()
    asyncio.run(main())
    e = time.time()
    print(e - s)
