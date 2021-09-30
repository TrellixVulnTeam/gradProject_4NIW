import Link from 'next/link'

const ProfileItem = ({profile}) => {
    return (
        <div className="mt-6">
            <div className="flex w-full items-center">
                <Link href="/profile/[id]" as={`/profile/${profile.id}`}>
                    <a className="flex items-center">
                        <img className="rounded-full w-24 h-24" src={profile.url_picture} alt="new" />
                        <h2 className="pl-6 font-bold">{profile.name}</h2>
                    </a>
                </Link>
           </div>
        </div>
    )
}

export default ProfileItem;