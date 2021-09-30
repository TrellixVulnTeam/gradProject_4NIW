import Link from 'next/link'
import { useRouter } from 'next/router';

const profile = ({profile}) => {
    // const router = useRouter()
    // const { id } = router.query

    return (
        <div>
            <h2>
                {profile.name}
            </h2>
            <p>
                This is a profile component {profile.id}
            </p>
            <Link href='/'>Go Back</Link>
        </div>
    )
}

export async function getServerSideProps(context) {
    const res = await fetch(`http://localhost:5000/profile/${context.params.id}`)

    const profile = await res.json()

    return {
        props: {
            profile
        }
    }
}

export default profile;