from good_info import Good, Goods

if __name__ == '__main__':
    file_name = input("Введите путь к файлу:")
    goods = Goods()
    goods.get_from_file(file_name)
    print(goods)


# def get_goods_info(goods_list):
#
#     result = {}
#     expensive_goods = set()
#     min_price = float('inf')
#     max_price = 0
#     goods_count = 0
#     price_sum = 0
#
#     for good in goods_list:
#         item = good.replace('\n', '').split(':')
#         item_price = int(item[1])
#         price_sum += item_price
#         if item_price < min_price:
#             min_price = item_price
#         elif item_price > max_price:
#             max_price = item_price
#         if item_price > 100:
#             expensive_goods.add(item[0])
#         goods_count += 1
#
#     mean_price = round(price_sum / goods_count, 2)
#
#     result['min_price'] = min_price
#     result['max_price'] = max_price
#     result['mean_price'] = mean_price
#     result['goods_count'] = goods_count
#     result['expensive_goods'] = expensive_goods
#
#     return result
#
#
# def print_goods_info(goods_list):
#
#     goods_dict = get_goods_info(goods_list)
#     expensive_goods = '\n'.join(list(goods_dict['expensive_goods']))
#
#     print(
#           f'Максимальная цена товара: {goods_dict["max_price"]}',
#           f'Миниимальная цена товара: {goods_dict["min_price"]}',
#           f'Средняя цена товара: {goods_dict["mean_price"]}',
#           f'Количество товаров: {goods_dict["goods_count"]}',
#           f'Дорогие товары:\n{expensive_goods}',
#           sep='\n'
#           )
#
#
# print_goods_info(goods_list)
