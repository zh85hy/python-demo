class InsertionSort(object):

    def sort(self, data):
        if data is None:
            raise TypeError('DATA cannot be None.')
        if len(data) < 2:
            return data
        for r in range(1, len(data)):
            for l in range(r):
                if data[r] < data[l]:
                    temp = data[r]
                    data[l+1:r+1] = data[l:r]
                    data[l] = temp
        return data


def main():
    data_list = [6, 5, 3, 1, 8, 7, 2, 4]
    is_instance = InsertionSort()
    print(is_instance.sort(data_list))

if __name__ == '__main__':
    main()
