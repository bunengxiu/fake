import random

import uvicorn
from fastapi import FastAPI

app = FastAPI()

category_number = 10
datasheet_number = 3
image_number = 3
multi = 10
vendor_id = 1
host = '0.0.0.0'
port = 60001
url_prefix = f'http://127.0.0.1:{port}/fake'


@app.get("/")
async def root():
    return {"message": "fake", 'version': '0.0.6'}


@app.get("/fake/category")
async def category():
    return {
        'res': 'ok',
        'category_url': [f'{url_prefix}/cate_{i + 1}' for i in range(category_number)]
    }


@app.get("/fake/list")
async def list_page(cate, page_number):
    c_n = int(cate.replace('cate_', ''))
    if int(page_number) > c_n:
        return {
            'res': 'ok',
            'category': cate,
            'detail_page_url': [],
            'total_page': c_n
        }
    return {
        'res': 'ok',
        'category': cate,
        'detail_page_url': [f'{url_prefix}/{cate}/detail_{i + 1}.json' for i in range(int(page_number) * multi)][-multi:],
        'total_page': c_n
    }


@app.get("/fake/detail")
async def detail_page(cate, detail_data):
    p_id = detail_data.replace('.json', '').replace('detail_', '')
    if int(p_id) > category_number * multi:
        return
    return {
        'res': 'ok',
        'detail_page_data': {
            'mpn': p_id,
            'sku': f'sku_{p_id}',
            'moq': f'moq_{p_id}',
            'packing': f'packing_{p_id}',
            'package': f'package_{p_id}',
            'category': [cate],
            'quantity': random.randint(1, 10),
            'vendor': f'vendor_{p_id}',
            'vendor_id': vendor_id,
            'datasheet': [f'{url_prefix}/{cate}/datasheet_{i + 1}' for i in range(datasheet_number)],
            'image_url': [f'{url_prefix}/{cate}/image_{i + 1}' for i in range(image_number)],
            'description': 'a b c d e f g h i j k l m n o p q r s t u v w x y z',
            'attributes': {
                'attribute1': f'attribute1_{p_id}',
                'attribute2': f'attribute2_{p_id}',
                'attribute3': f'attribute3_{p_id}',
                'attribute4': f'attribute4_{p_id}',
                'attribute5': f'attribute5_{p_id}'
            },
            'distributor_url': f'{url_prefix}/{cate}/{detail_data}',
            'product_detail_url': f'{url_prefix}/{cate}/{detail_data}'
        }
    }


if __name__ == '__main__':
    uvicorn.run('run:app',
                host=host,
                port=port
                )
