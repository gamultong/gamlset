"""
테스트 실행 엔트리포인트
Usage: python -m tests.run
"""
from .test_gamlset import GamlSet_TestCase

if __name__ == '__main__':
    from unittest import main
    main()