from time import perf_counter


def benchmark(repeat=100):
    def benchmark_inner(fn):
        def inner(*args, **kwargs):
            measure = []
            for _ in range(repeat):
                t0 = perf_counter()
                fn(*args, **kwargs)
                t1 = perf_counter()
                measure.append(t1 - t0)
            print(f"mean dt for {fn.__name__}: ", sum(measure) / repeat)

        return inner

    return benchmark_inner
