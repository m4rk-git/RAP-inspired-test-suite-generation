from data.complicated_tests.textwrap import *
import pytest
from textwrap import wrap as std_wrap, fill as std_fill

def test_wrap():
    assert wrap("Hello there -- you goof-ball, use the -b option!") == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=10) == [
        "Hello there",
        "-- you goof-ball,",
        "use the -b",
        "option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=20) == [
        "Hello there -- you",
        "goof-ball, use the",
        "-b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=30) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=40) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=50) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=60) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=70) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=80) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=90) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=100) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=110) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=120) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=130) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=140) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=150) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=160) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=170) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=180) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=190) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=200) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=210) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=220) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=230) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=240) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=250) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=260) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=270) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=280) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=290) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=300) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=310) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=320) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=330) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=340) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=350) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=360) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=370) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=380) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=390) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=400) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=410) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=420) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=430) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=440) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=450) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=460) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=470) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=480) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=490) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=500) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=510) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=520) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=530) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=540) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=550) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=560) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=570) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=580) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=590) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=600) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=610) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=620) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=630) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=640) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=650) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=660) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=670) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=680) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=690) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=700) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=710) == [
        "Hello there -- you goof-ball, use the -b option!"
    ]
    assert wrap("Hello there -- you goof-ball, use the -b option!", width=720) == [
        "Hello there -- you