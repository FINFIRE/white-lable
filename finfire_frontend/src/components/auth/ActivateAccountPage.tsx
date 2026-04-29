import { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import * as authApi from '../../api/auth';
import BrandLogo from '../layout/BrandLogo';

const ActivateAccountPage: React.FC = () => {
  const { uid, token } = useParams<{ uid: string; token: string }>();
  const [status, setStatus] = useState<'loading' | 'success' | 'error'>(
    'loading'
  );
  const [errorMsg, setErrorMsg] = useState('');

  useEffect(() => {
    if (!uid || !token) {
      setStatus('error');
      setErrorMsg('Invalid activation link.');
      return;
    }

    authApi
      .activateAccount(uid, token)
      .then(() => setStatus('success'))
      .catch((err: unknown) => {
        setStatus('error');
        if (
          err &&
          typeof err === 'object' &&
          'response' in err &&
          (err as { response?: { data?: Record<string, string[]> } }).response
            ?.data
        ) {
          const responseData = (
            err as { response: { data: Record<string, string[]> } }
          ).response.data;
          const messages = Object.values(responseData).flat().join(' ');
          setErrorMsg(messages || 'Activation failed.');
        } else {
          setErrorMsg('Activation failed. The link may have expired.');
        }
      });
  }, [uid, token]);

  return (
    <div className="flex min-h-screen items-center justify-center bg-gradient-to-br from-primary-50 via-white to-primary-100">
      <div className="w-full max-w-md rounded-2xl bg-white p-8 shadow-lg shadow-primary-200/40 text-center">
        <div className="mb-6 flex justify-center">
          <BrandLogo className="h-12 w-auto" />
        </div>

        {status === 'loading' && (
          <p className="text-sm text-text-secondary">
            Activating your account...
          </p>
        )}

        {status === 'success' && (
          <div className="rounded-lg border border-green-200 bg-green-50 px-4 py-3 text-sm text-green-700">
            Your account has been activated! You can now log in.
          </div>
        )}

        {status === 'error' && (
          <div className="rounded-lg border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700">
            {errorMsg}
          </div>
        )}

        <p className="mt-6 text-sm text-text-secondary">
          <Link
            to="/login"
            className="font-medium text-primary-500 hover:text-primary-700 hover:underline"
          >
            Go to Login
          </Link>
        </p>
      </div>
    </div>
  );
};

export default ActivateAccountPage;
