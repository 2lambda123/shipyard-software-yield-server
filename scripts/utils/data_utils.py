import ast

import numpy as np
import pandas as pd


def replace_null_values(x: str) -> str:
    if x == "[null]":
        return "[]"
    elif x == "[null,null]":
        return "[]"
    elif "null," in x:
        return x.replace("null,", "")
    elif ",null" in x:
        return x.replace(",null", "")
    else:
        return x

def filter_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df[
        ~((df["apy"].isnull()) & (df["apyReward"].isnull()) & (df["apyBase"].isnull()))
    ]
    df = df[(df["apy"] >= 0) & (df["apy"] <= 1e6) & (df["tvlUsd"] >= 1000) & (df["tvlUsd"] <= 2e10)]
    exclude_pools = [
        "0xf4bfe9b4ef01f27920e490cea87fe2642a8da18d",
        "DWmAv5wMun4AHxigbwuJygfmXBBe9WofXAtrMCRJExfb",
        "ripae-seth-weth-42161",
        "ripae-peth-weth-42161",
        "0x3eed430cd45c5e2b45aa1adc609cc77c6728d45b",
        "0x3c42B0f384D2912661C940d46cfFE1CD10F1c66F-ethereum",
        "0x165ab553871b1a6b3c706e15b6a7bb29a244b2f3",
    ]
    df = df[~df["pool"].isin(exclude_pools)]
    df = df[df["project"] != "koyo-finance"]
    return df

def round_values(df: pd.DataFrame) -> pd.DataFrame:
    apy_columns = ["apy", "apyBase", "apyReward"]
    df[apy_columns] = df[apy_columns].round(5)
    return df

def exclude_pools_and_projects(df: pd.DataFrame) -> pd.DataFrame:
    exclude_pools = [
        "0xf4bfe9b4ef01f27920e490cea87fe2642a8da18d",
        "DWmAv5wMun4AHxigbwuJygfmXBBe9WofXAtrMCRJExfb",
        "ripae-seth-weth-42161",
        "ripae-peth-weth-42161",
        "0x3eed430cd45c5e2b45aa1adc609cc77c6728d45b",
        "0x3c42B0f384D2912661C940d46cfFE1CD10F1c66F-ethereum",
        "0x165ab553871b1a6b3c706e15b6a7bb29a244b2f3",
    ]
    df = df[~df["pool"].isin(exclude_pools)]
    df = df[df["project"] != "koyo-finance"]
    return df
