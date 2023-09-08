from django.conf import settings

file_path = f"{settings.BASE_DIR}/jobs/fixtures/indeed/"
file_names = [
    "search-results-short",
    "search-results-full",
    "search-results-full-mosaic",
    "job-details-1",
    "job-details-2",
    # "q-python-django-l-remoto",
    # "q-python-django-l",
]

pages = {}
for name in file_names:
    path = f"{file_path}{name}.html"
    with open(path, "r") as file:
        page = file.read()
        pages[name] = page

job_details = {}
job_details["job-details-1"] = {
    "html": "",
    "url": "",
    "title": "Vaga Estágio 1",
    "company_info": "Empresa 1\n\n\nRemoto",
    "apply_url": "",
    "benefits": "",
    "description": "Lorem Ipsum.\n Responsabilidades e atribuições\n\n\n Responsabilidade 1;\n Responsabilidade 2;\n\n\n Requisitos e qualificações\n\n\n Requisito 1;\n Requisito 2;",
}
job_details["job-details-2"] = {
    "html": "",
    "url": "",
    "title": "Vaga Estágio 2",
    "company_info": "Empresa 2\n\n\nRemoto",
    "apply_url": "",
    "benefits": "",
    "description": "Lorem Ipsum 2.\nResponsabilidades e atribuições\n\n Responsabilidade 1;\n Responsabilidade 2;",
}

mosaic_jobcards = {}
mosaic_jobcards["search-results-full-mosaic"] = [
    {
        "jobkey": "e26115205e088e41",
        "url": "/viewjob?jk=e26115205e088e41",
        "title": "Pessoa Desenvolvedora Python - Trabalho Remoto",
        "company": "BairesDev",
        "location": "Jaboatão dos Guararapes, PE",
        "relative_time": "há 2 dias",
    },
    {
        "jobkey": "b37faa847e3d88ae",
        "url": "/viewjob?jk=b37faa847e3d88ae",
        "title": "Software Engineer Python - Remote",
        "company": "BairesDev",
        "location": "Recife, PE",
        "relative_time": "há 2 dias",
    },
    {
        "jobkey": "2e2b6281f4ea3612",
        "url": "/viewjob?jk=2e2b6281f4ea3612",
        "title": "Desenvolvedor Python autêntico - Trabalho Remoto",
        "company": "BairesDev",
        "location": "Jaboatão dos Guararapes, PE",
        "relative_time": "há 2 dias",
    },
    {
        "jobkey": "3e6e99551e6bb084",
        "url": "/viewjob?jk=3e6e99551e6bb084",
        "title": "Software Developer Python - REMOTE WORK",
        "company": "BairesDev",
        "location": "Recife, PE",
        "relative_time": "há 2 dias",
    },
    {
        "jobkey": "46521c4677e9ed95",
        "url": "/viewjob?jk=46521c4677e9ed95",
        "title": "Python Specialist (Remote)",
        "company": "BairesDev",
        "location": "Recife, PE",
        "relative_time": "há 2 dias",
    },
    {
        "jobkey": "9c30d9b03023465e",
        "url": "/viewjob?jk=9c30d9b03023465e",
        "title": "Python Analyst - Remote",
        "company": "BairesDev",
        "location": "Recife, PE",
        "relative_time": "há 2 dias",
    },
    {
        "jobkey": "0228dbe98d2503f5",
        "url": "/viewjob?jk=0228dbe98d2503f5",
        "title": "Senior Python Developer - REMOTE WORK |LATAM|",
        "company": "BairesDev",
        "location": "Recife, PE",
        "relative_time": "há 2 dias",
    },
    {
        "jobkey": "cd1c5cfa50fd17af",
        "url": "/viewjob?jk=cd1c5cfa50fd17af",
        "title": "Desenvolvedor Python Pleno",
        "company": "Koopere Cooperativa | Supero Soluções",
        "location": "Remoto",
        "relative_time": "há 30+ dias",
    },
    {
        "jobkey": "1331a3559e7757f3",
        "url": "/viewjob?jk=1331a3559e7757f3",
        "title": "Python + VueJS Developer - REMOTE WORK",
        "company": "BairesDev",
        "location": "Recife, PE",
        "relative_time": "há 2 dias",
    },
    {
        "jobkey": "4a90a32fdadaf434",
        "url": "/viewjob?jk=4a90a32fdadaf434",
        "title": "Python Tech Lead / Research + Development - Remote Work",
        "company": "BairesDev",
        "location": "Recife, PE",
        "relative_time": "há 2 dias",
    },
    {
        "jobkey": "2d7625363b2ecd5b",
        "url": "/viewjob?jk=2d7625363b2ecd5b",
        "title": "Python + React Developer - REMOTE WORK",
        "company": "BairesDev",
        "location": "Recife, PE",
        "relative_time": "há 2 dias",
    },
    {
        "jobkey": "ee2e0045fe3f6397",
        "url": "/viewjob?jk=ee2e0045fe3f6397",
        "title": "Bulk Email Python - Remoote",
        "company": "BairesDev",
        "location": "Recife, PE",
        "relative_time": "há 2 dias",
    },
    {
        "jobkey": "3b5852078a6494bd",
        "url": "/viewjob?jk=3b5852078a6494bd",
        "title": "Desenvolvedor python senior",
        "company": "Netvagas - (21734898)",
        "location": "São Paulo, SP",
        "relative_time": "Hoje",
    },
    {
        "jobkey": "932e2aa472304c4f",
        "url": "/viewjob?jk=932e2aa472304c4f",
        "title": "Data Engineer - X Delivery",
        "company": "Boston Consulting Group",
        "location": "São Paulo, SP",
        "relative_time": "há 30+ dias",
    },
    {
        "jobkey": "ff79443a79d92566",
        "url": "/viewjob?jk=ff79443a79d92566",
        "title": "Pessoa desenvolvedora fullstack (python / angular) pleno",
        "company": "Netvagas - (64172998)",
        "location": "Florianópolis, SC",
        "relative_time": "Hoje",
    },
]


job_cards = {}
job_cards["search-results-short"] = [
    {
        "title": "Estagiário de Dados e MIS",
        "data-jk": "ce75845b0f6a82e3",
        "href": "/pagead/clk?mo=r&ad=-6NYlbfkN0DcjF4Y0eKv0CsWWlZ5x9FrC41SbkkqrPAuVGRE_5Udo6HU-pVpgJFNdcRqGotqWyzs3qIxTfs5G6XJtrjkCjVZNinEjjfR1q4VG4U8NdRlJZp_c-Asb_3XeegoxnNwDktvRqxnRM7pnD9Y5GYFxW5ZdB4Yjugaf6vj5gNkFpugHgwfrk0gmeU010KVlzqYWvlu9DAqvo_bwRXN6BGzFost7p5ZYFnTAgzorT19qmkkR2QsIBQDY7cN8_fRBp8ztqJ4epu97hs3esFg70umKZyMk2RsTQd16LOG8rs7Xj0Kcn8HOV178E2gqp53_trM30hktaDIAehHQ2LPISIkm1-pjs8XACH_sUOO-nJ85bXtinnuEYtMYAoqmOPYWKQc8UlYORWU-DnQaauujhEXMXS-6U7XG875vv8k4zbEto0rDTsIRwC__jHs-AeqojExL_kuMXNqnrekIOT4SvAXolhEGnFg6IwJkmYk_Kox3JlnnGoOYoxjeYvNXonJYuWhLrUyKKWn6LrADCtBvvBeFTUrK1c_Zr3hFIkXiJXOlcnICordGyCihhNb7ys031K50fSeb4j_wFdffA==&xkcb=SoAU-_M3LhNgu-QiyB0IbzkdCdPP&p=0&fvj=0&vjs=3",
        "company_name": "Digio",
        "company_location": None,
    },
    {
        "title": "Cientista De Dados Júnior",
        "data-jk": "5d482db843f4b802",
        "href": "/pagead/clk?mo=r&ad=-6NYlbfkN0DK20QmcZKVx9LjbuC-u5lB3rxeJCP2k8q23I1ohXQB_Ju63qY-73nzSCYa_ovISxbTFJwYvE9qLAaUXpiMGF-XYX_0zZxmDXqyUrn9EaJ8gKzIOVeke5-ziMTXuFL7X30LDQvNH76OAfFA2PrgoJaH0azfzyG1CRbEgEV6rb5aPBTxFUDIiHZG86fFOOX1Qc-9VjRjVjduQuuPSnbmNHlrhIYJhjAdvLQyhLvoyAxsNVAycNwVwhHakeTSSShyFf1kVJKJMK5t7gMbjWEAIi4wrsSYJnkVDn7-uZra_O7FjkcRkplyP7LMBASZ-0YnZ99NcVUBSpAst3QU624PAtncnnGgWkoLZHxBzIaolxVmdoGN5ZodJ2VhgGeIHk9FG8bTBCKgDFOVCtS-AxF8NQ10v_JWQUQKQbv91lX8rYIg7i7KtZv2dKKH2waBGHHa0JU6bkIvC7ZfCQiSlcix30Ec-vGNtNHMpb1SuLU5r6W3dETJ4_UI-s4Wzeu2h0cYiHoNI4r5cbOUYNqnihbrQQQJDSK3R8SnWXSgRxT0CvYVfoZ03McEieH0n5DXNvUSEIA=&xkcb=SoCa-_M3LhNgu-QiyB0PbzkdCdPP&p=1&fvj=0&vjs=3",
        "company_name": "Claro",
        "company_location": "São Paulo, SP",
    },
]
job_cards["search-results-full"] = [
    {
        "title": "Estagiário de Dados e MIS",
        "data-jk": "ce75845b0f6a82e3",
        "href": "/pagead/clk?mo=r&ad=-6NYlbfkN0DcjF4Y0eKv0CsWWlZ5x9FrC41SbkkqrPAuVGRE_5Udo6HU-pVpgJFNdcRqGotqWyzs3qIxTfs5G6XJtrjkCjVZNinEjjfR1q4VG4U8NdRlJZp_c-Asb_3XeegoxnNwDktvRqxnRM7pnD9Y5GYFxW5ZdB4Yjugaf6vj5gNkFpugHgwfrk0gmeU010KVlzqYWvlu9DAqvo_bwRXN6BGzFost7p5ZYFnTAgzorT19qmkkR2QsIBQDY7cN8_fRBp8ztqJ4epu97hs3esFg70umKZyMk2RsTQd16LOG8rs7Xj0Kcn8HOV178E2gqp53_trM30hktaDIAehHQ2LPISIkm1-pjs8XACH_sUOO-nJ85bXtinnuEYtMYAoqmOPYWKQc8UlYORWU-DnQaauujhEXMXS-6U7XG875vv8k4zbEto0rDTsIRwC__jHs-AeqojExL_kuMXNqnrekIOT4SvAXolhEGnFg6IwJkmYk_Kox3JlnnGoOYoxjeYvNXonJYuWhLrUyKKWn6LrADCtBvvBeFTUrK1c_Zr3hFIkXiJXOlcnICordGyCihhNb7ys031K50fSeb4j_wFdffA==&xkcb=SoAU-_M3LhNgu-QiyB0IbzkdCdPP&p=0&fvj=0&vjs=3",
        "company_name": "Digio",
        "company_location": None,
    },
    {
        "title": "Cientista De Dados Júnior",
        "data-jk": "5d482db843f4b802",
        "href": "/pagead/clk?mo=r&ad=-6NYlbfkN0DK20QmcZKVx9LjbuC-u5lB3rxeJCP2k8q23I1ohXQB_Ju63qY-73nzSCYa_ovISxbTFJwYvE9qLAaUXpiMGF-XYX_0zZxmDXqyUrn9EaJ8gKzIOVeke5-ziMTXuFL7X30LDQvNH76OAfFA2PrgoJaH0azfzyG1CRbEgEV6rb5aPBTxFUDIiHZG86fFOOX1Qc-9VjRjVjduQuuPSnbmNHlrhIYJhjAdvLQyhLvoyAxsNVAycNwVwhHakeTSSShyFf1kVJKJMK5t7gMbjWEAIi4wrsSYJnkVDn7-uZra_O7FjkcRkplyP7LMBASZ-0YnZ99NcVUBSpAst3QU624PAtncnnGgWkoLZHxBzIaolxVmdoGN5ZodJ2VhgGeIHk9FG8bTBCKgDFOVCtS-AxF8NQ10v_JWQUQKQbv91lX8rYIg7i7KtZv2dKKH2waBGHHa0JU6bkIvC7ZfCQiSlcix30Ec-vGNtNHMpb1SuLU5r6W3dETJ4_UI-s4Wzeu2h0cYiHoNI4r5cbOUYNqnihbrQQQJDSK3R8SnWXSgRxT0CvYVfoZ03McEieH0n5DXNvUSEIA=&xkcb=SoCa-_M3LhNgu-QiyB0PbzkdCdPP&p=1&fvj=0&vjs=3",
        "company_name": "Claro",
        "company_location": "São Paulo, SP",
    },
    {
        "title": "Pessoa Desenvolvedora Python",
        "data-jk": "f73901633f380574",
        "href": "/rc/clk?jk=f73901633f380574&fccid=583060e2f53a02f1&vjs=3",
        "company_name": "Confi",
        "company_location": None,
    },
    {
        "title": "Analista de Dados Júnior",
        "data-jk": "a3d715b1f1e8582a",
        "href": "/pagead/clk?mo=r&ad=-6NYlbfkN0AmaNMv4sr92vlelJD9HsDFX9e0FVUO2yM-5PrIgeUEryFidD_uEQ4rbuAgRgn_FAO66Rx53DBUFvrm05PnoebPzplv4qVkivz8yfwb0_vohsL6UwGz5PapcdAoaFkEnxdl8jGPv07Rztfkuv39CF-hXSI2SlGgY77XoHmSzUuYe8DPTZaRxf0MEvk-3cJMTg3yE93QWSYn7wX_VAlED5zbBeMlokF5tCLmd_pyyErs6pvnlv5juRtYUmuZ_WX-2U33c9WU3sMeePU_kEIUTMhKzVzMCcRk8qIY3H4m1uJakyMSj46PDZIDma4hdFEA4ZVuY0Y9b2CYh6zIImt4QVW7hSIO4H_TsDyBa7-1h2EtQzZS5l5Ke1KkzMEvnDbXOlIQjcUDgYe8aHFU799ZoUXtQCo1lb66aJ9LzT8kLK_ikqa5ARdfe66HU8-adJHNBynnoDsWjITDUk4xwZp9MyucHLmkiwELll-lpQyBv-ln_-W6TS2etUjESrhiyoweJ4319TnKTrz9QGTrGRNVXKpHUOmUyclSwlff1IfNAj6vouAMB5IG-5KnpBt3OfY7aRHcsoqaCrB8l-Taq5oIxdCb6_XgjAWLhHyav4mhIvHEkUiXdUBxoY_m5BeFNDCPc5Uumi16vs_GslwFyh5ExfCvucUCphH04WkvJEZJwdjy8gtYE_liUOnpCeP9rkH03hByH9Njds0zTA9abKeS7fzWe7SQh0HE2wUwVojEaFIlg1_ugdAZaVhVf6nU5D8oNLd0IvpGoiqcSAlSObkmDyUwQnO3kFEHZstLzOwjPU9_tYPwKKhSarz-smMbYRbQutuReWagYwnF8yNjgjcyCBUYJoDnurHvFSk2KUPF1GSItNfQi3ylpEFG2rcfh_4Pww19CzYEg1ZRWkzgsQ3WpXeOVQkHjGYzDJsO22ZXEMINYCCxH7osIBTFCmbQ0GsY28huj-j5E6g3ARFpv-Icbp_V&xkcb=SoCz-_M3LhNgu-QiyB0NbzkdCdPP&p=3&fvj=0&vjs=3",
        "company_name": "Locaweb",
        "company_location": "Remoto híbrido in São Paulo, SP",
    },
    {
        "title": "Analista de Banco de Dados Jr - Movilway - Remoto",
        "data-jk": "556711e3020bb416",
        "href": "/rc/clk?jk=556711e3020bb416&fccid=f3b54fe6f4411105&vjs=3",
        "company_name": "Movilway",
        "company_location": None,
    },
    {
        "title": "Desenvolvedor(a) em Python (Plataforma de Dados)",
        "data-jk": "28f5305d8cb6e15a",
        "href": "/rc/clk?jk=28f5305d8cb6e15a&fccid=d440598bc246c586&vjs=3",
        "company_name": "Vertigo Tecnologia",
        "company_location": None,
    },
    {
        "title": "Analista de Dados (Python)",
        "data-jk": "ea57af711ff6c823",
        "href": "/rc/clk?jk=ea57af711ff6c823&fccid=a623d38851ccc739&vjs=3",
        "company_name": "Join Tecnologia &Design",
        "company_location": None,
    },
    {
        "title": "Analista de Dados",
        "data-jk": "fb0ae305a5423be9",
        "href": "/pagead/clk?mo=r&ad=-6NYlbfkN0AmaNMv4sr92vlelJD9HsDFX9e0FVUO2yM-5PrIgeUEryFidD_uEQ4rbuAgRgn_FAMczWYqqojfAVDGxxXapBSFQEWOWAlEIvnCQsSiDMQQYk4ZHSUr5YJMSkMoBb6yY--8zr9M-zvjleSN6G09mla_VcNAZF1MOZPykGBXcPx3UguGH4yFEoFL-05Ghh9TenYzjl8ZVZIqYIN1A_qIAEelmOx6wF6ncZuUjXDsPwmipz-QMrAjFNh3NNwWPKCeLL3fKwxQRTFuGre3rheTNB9LEh30FvfnctdvTxETiT2uHTofKD0l0OlhI52IHsO0n_jPXuV3B-Wax8u0B_7I_m9leMaJ_kNhkxalc57ERiBtdyfZfiIjFXGQJYs6FVeUapysz_c1QC0svfDXoy2qybmYusNQGSfdshlgF_ad5j0oXlGPplpvV1pRrhgOUDl5TFjpf7vEYJebwpJc8x6cqTkUuJRbRblh9Py4MRzfIwx3GuXMZmBF0EMQMJfzKt1a2Wexunn3UDKuMmcZ3D52dPohpFDF3kRM_8Fs3PLShHeXQ3w-7VW_LA0Y2VX5RS7lUQpi3Z5k6Ka-NpgA_xuSH5VtokHH2pXE0hySJt7OAZxm1-n8ry7lMxY5XuD-u_PpgFvKERzuiPyhzwMXplsySj3FJhP3qKeQNd2-gyZ5Hw5bYbyncPq1PVqPsg1dedQB0nm3gAIYvF6Mkhiqie66JNm3LD5ugP6o1aNXdbVIQuStK6D7tR6TLZWpL9x1SEnMwk1iVakhJPqZJATatfk75KAX59vbnYsI-kDKpnctuEYiIYbwTDVC8FzKYW3g6bAWUJ9Nu79SmLbHIIg1hDxBFQFdbLgYupjealaOdF0i802uBIZwRnNQlLq3esgqVXNhUtRFNLtpXP7AbjTTgDZARpcFrXfl1xhSsY9e4ZLcovE0FIuNWrWUUNSgXwC0e4poqQ9TMFIYQqg70Q==&xkcb=SoDH-_M3LhNgu-QiyB0BbzkdCdPP&p=7&fvj=0&vjs=3",
        "company_name": "Curriculum.com.br",
        "company_location": None,
    },
    {
        "title": "Estágio em Desenvolvimento Mobile",
        "data-jk": "a1a1bb3d2df5ac45",
        "href": "/rc/clk?jk=a1a1bb3d2df5ac45&fccid=b1bd5cd18584fd5d&vjs=3",
        "company_name": "SenseData",
        "company_location": None,
    },
    {
        "title": "Analista dados I",
        "data-jk": "46b76deec3bf825f",
        "href": "/rc/clk?jk=46b76deec3bf825f&fccid=724f5a53e81ef8f8&vjs=3",
        "company_name": "Grupo RBS",
        "company_location": None,
    },
    {
        "title": "CIENTISTA DE DADOS PL - REMOTO",
        "data-jk": "6f506d4ab1f20cad",
        "href": "/rc/clk?jk=6f506d4ab1f20cad&fccid=4df8c09240f8f9eb&vjs=3",
        "company_name": "NAVA | Technology for Business",
        "company_location": None,
    },
    {
        "title": "Cientista de dados pl (remoto) (1)",
        "data-jk": "eb71820e3308bd43",
        "href": "/rc/clk?jk=eb71820e3308bd43&fccid=dd616958bd9ddc12&vjs=3",
        "company_name": "Netvagas - (629550829)",
        "company_location": None,
    },
    {
        "title": "Especialista Sistemas Da Informações Pleno",
        "data-jk": "48c5891bbf92dcd6",
        "href": "/pagead/clk?mo=r&ad=-6NYlbfkN0DK20QmcZKVx9LjbuC-u5lB3rxeJCP2k8q23I1ohXQB_Ju63qY-73nzSCYa_ovISxYCFPrtLWQPAJheyqJczT01YW7fkRvSAKkueuyIwz0wg2reY8Upmf_sKN4yz-9yAD9f2oKXM2S6OqExvwzp0lb7IZtweCxRFEYWbNjOujOZK7eeQpe5YbiHa_mXi-yk9K_Ail-3gyUrs0QRRjrgBaJyPua-kFn2rYgE9wEAh12pKhySVYXQq_cVNVvYjmuM5dkZKoDq4gFL6ioyeWHQHcXy8NT-sJaWOg6hWZw30vkhcwLD4P2PxvGYO7udqhApnZkO2rv0-kf6HONZmiIyaWOrxsUKb9PoG8BR5oBDY1jzQnfduKGUJ4fp1XrTEKAZVRbyKL3T3EAGKcMiwww9pyxTxH0-1kYnbXRORPnZcQr012KmZN73LXJIfHvur9dys7kkS72s10_jw09sqvFjm-OkfJjQmFvxaOcL-_RVHApglcAk856shEUpKrxSmEwZW2DDMoRZBiUR3MbhOuTrK4U0xwExMwA10Edg_lZYVbVOs3OqNFSImgXY3nzSuNkLVRM=&xkcb=SoBH-_M3LhNgu-QiyB0bbzkdCdPP&p=12&fvj=0&vjs=3",
        "company_name": "Claro",
        "company_location": "São Paulo, SP",
    },
    {
        "title": "Desenvolvedor Python",
        "data-jk": "cba40857b488f004",
        "href": "/company/Innolevels/jobs/Python-cba40857b488f004?fccid=b98f3184c24b89e7&vjs=3",
        "company_name": "Innolevels",
        "company_location": "Home office in São Paulo, SP",
    },
    {
        "title": "Pessoa Cientista de Dados",
        "data-jk": "4eb78f0c67009c5e",
        "href": "/rc/clk?jk=4eb78f0c67009c5e&fccid=1e9636cf35f06baa&vjs=3",
        "company_name": "alt.bank",
        "company_location": None,
    },
]
