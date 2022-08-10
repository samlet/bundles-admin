from bluecc.bundles.bundles_bridge import BundlesBridgeConnector


class BundlesCli(object):
    def __int__(self):
        # self.bridge=BundlesBridgeConnector()
        pass

    def version(self):
        """
        $ python -m bluecc.bundles.bundles_cli version
        :return:
        """
        bridge = BundlesBridgeConnector()
        print(bridge.version)
        # print('1.0')

if __name__ == '__main__':
    import fire
    fire.Fire(BundlesCli)

