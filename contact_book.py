import pandas as pd
import os
from typing import List, Dict, Optional


class ContactBook:
    def __init__(self, resource_file_path: str):
        self._res_file_path = resource_file_path
        self._df = self._load_from_file()

    def add_contact(self, name: str, contact_number: str, email_id: str, address: str) -> None:
        row = {
            "name": name,
            "contact_number": contact_number,
            "email_id": email_id,
            "address": address
        }
        self._df = self._df.append(row, ignore_index=True)
        self._df.to_csv(self._res_file_path, index=False)

    def edit_contact(self, name: str, new_name: Optional[str], new_contact_number: Optional[int],
                     new_email_id: Optional[str],
                     new_address: Optional[str]) -> None:
        idx = self._df.loc[self._df.name == name].index
        idx = idx[0]
        if new_name is not None:
            self._df.loc[idx, "name"] = new_name
        if new_contact_number is not None:
            self._df.loc[idx, "contact_number"] = new_contact_number
        if new_email_id is not None:
            self._df.loc[idx, "email_id"] = new_email_id
        if new_address is not None:
            self._df.loc[idx, "address"] = new_address

        self._df.to_csv(self._res_file_path, index=False)

    def delete_contact(self, name: str) -> None:
        self._df.drop(self._df[self._df.name == name].index, inplace=True)
        self._df.to_csv(self._res_file_path, index=False)

    def search_contact(self, name: str) -> List[Dict]:
        res = []
        df = self._df[self._df.name == name]
        for _, row in df.iterrows():
            res.append(dict(row))
        return res

    def display_contact_book(self) -> List[Dict]:
        res = []
        self._df.sort_values("name", inplace=True)
        for _, row in self._df.iterrows():
            res.append(dict(row))

        return res

    def is_name_in_contact_book(self, name: str) -> bool:
        return name in self._df["name"].values

    def _load_from_file(self) -> pd.DataFrame:
        if os.path.exists(self._res_file_path):
            return pd.read_csv(self._res_file_path)

        return pd.DataFrame(columns=["name", "contact_number", "email_id", "address"])
