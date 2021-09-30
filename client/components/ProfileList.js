import ProfileItem from "../components/ProfileItem";
import Pagination from "./Pagination";
import { useState } from "react";

const ProfileList = ({ profiles, currentPage, nextPage, lastPage }) => {
  return (
    <div>
      {profiles.map((profile) => (
        <ProfileItem profile={profile} />
      ))}
    </div>
  );
};

export default ProfileList;
