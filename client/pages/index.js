import Head from "next/head";
import Image from "next/image";
import Link from "next/link";
import Searchbar from "../components/Searchbar";
import { useState } from "react";
import RandomProfiles from "../components/RandomProfiles";

export default function Home({ randomProfiles, topics1, topics2 }) {
  const [whatToSearch, setWhatToSearch] = useState("profiles");
  const [readMore, setReadMore] = useState(false);
  const [searchText, setSearchText] = useState("");

  const extraContent = (
    <div>
      <ul className="flex flex-wrap space-x-24">
        {topics2.map((topic) => (
          <li>
            <Link href="#">
              <a className="hover:text-blue-500">{topic.name}</a>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );

  const linkName = readMore ? "Read Less" : "Read More";

  return (
    <div className="w-3/4">
      <Searchbar searchText={searchText} setSearchText={setSearchText} />

      <div className="mt-3 flex">
        <span className="text-gray-500 mr-2">Search by: </span>

        {whatToSearch === "profiles" ? (
          <div>
            <a
              onClick={() => setWhatToSearch("profiles")}
              className="mr-2 text-blue-500 cursor-pointer"
            >
              profiles
            </a>
            <span className="text-gray-500 ">|</span>
            <a
              onClick={() => setWhatToSearch("publications")}
              className="ml-2 cursor-pointer"
            >
              publications
            </a>
          </div>
        ) : (
          <div>
            <a
              onClick={() => setWhatToSearch("profiles")}
              className="mr-2 cursor-pointer"
            >
              profiles
            </a>
            <span className="text-gray-500 ">|</span>
            <a
              onClick={() => setWhatToSearch("publications")}
              className="ml-2 text-blue-500 cursor-pointer"
            >
              publications
            </a>
          </div>
        )}
      </div>

      <div className="mt-6">
        <ul className="flex flex-wrap space-x-24">
          {topics1.map((topic) => (
            <li>
              <Link href="#">
                <a className="hover:text-blue-500">{topic.name}</a>
              </Link>
            </li>
          ))}
        </ul>
        {readMore && extraContent}
        <a
          className="text-blue-500 cursor-pointer"
          onClick={() => setReadMore(!readMore)}
        >
          {linkName}
        </a>
      </div>

      <div className="flex bg-blue-200 mt-6">
        <RandomProfiles randomProfiles={randomProfiles} />
        <div className="w-1/2">bye</div>
      </div>
    </div>
  );
}

export async function getStaticProps(context) {
  const res2 = await fetch(`http://localhost:5000/topic`);
  const topics = await res2.json();

  const res = await fetch(`http://localhost:5000/profile/random`);
  const randomProfiles = await res.json();

  const halfTopicLength = Math.floor(topics.length / 2);
  const topics1 = topics.slice(0, halfTopicLength);
  const topics2 = topics.slice(halfTopicLength, topics.length);

  return {
    props: {
      topics1,
      topics2,
      randomProfiles,
    },
  };
}
