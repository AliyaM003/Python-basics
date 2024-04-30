class Camera:
    def __init__(self, camera_id, location, status):
        self.camera_id = camera_id
        self.location = location
        self.status = status  # e.g., 'Active', 'Inactive'

class Footage:
    def __init__(self, footage_id, camera_id, timestamp, data):
        self.footage_id = footage_id
        self.camera_id = camera_id
        self.timestamp = timestamp
        self.data = data  # Placeholder for footage data

class CameraManager:
    def __init__(self):
        self.cameras = {}
        self.footages = {}

    def add_camera(self, camera_id, location, status):
        if camera_id in self.cameras:
            print("Camera already exists.")
        else:
            self.cameras[camera_id] = Camera(camera_id, location, status)
            print("Camera added successfully.")

    def update_camera(self, camera_id, location=None, status=None):
        if camera_id in self.cameras:
            if location:
                self.cameras[camera_id].location = location
            if status:
                self.cameras[camera_id].status = status
            print("Camera updated successfully.")
        else:
            print("Camera not found.")

    def delete_camera(self, camera_id):
        if camera_id in self.cameras:
            del self.cameras[camera_id]
            print("Camera deleted successfully.")
        else:
            print("Camera not found.")

    def display_cameras(self):
        if self.cameras:
            for camera in self.cameras.values():
                print(f"ID: {camera.camera_id}, Location: {camera.location}, Status: {camera.status}")
        else:
            print("No cameras available.")

    def add_footage(self, footage_id, camera_id, timestamp, data):
        if footage_id in self.footages:
            print("Footage already exists.")
        elif camera_id not in self.cameras:
            print("Camera ID not found.")
        else:
            self.footages[footage_id] = Footage(footage_id, camera_id, timestamp, data)
            print("Footage added successfully.")

    def monitor_surveillance_cameras(self, camera_id):
        if camera_id in self.cameras:
            print(f"Monitoring camera {camera_id} at {self.cameras[camera_id].location}")
        else:
            print("Camera not found.")

    def review_camera_footage(self, footage_id):
        if footage_id in self.footages:
            footage = self.footages[footage_id]
            print(f"Reviewing footage {footage.footage_id} from camera {footage.camera_id}")
        else:
            print("Footage not found.")

def main():
    manager = CameraManager()
    while True:
        print("\n1. Add Camera")
        print("2. Update Camera")
        print("3. Delete Camera")
        print("4. Display Cameras")
        print("5. Monitor Camera")
        print("6. Review Footage")
        print("7. Add Footage")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            camera_id = input("Enter camera ID: ")
            location = input("Enter camera location: ")
            status = input("Enter camera status (Active/Inactive): ")
            manager.add_camera(camera_id, location, status)
        elif choice == '2':
            camera_id = input("Enter camera ID: ")
            location = input("Enter new location (press enter to skip): ")
            status = input("Enter new status (Active/Inactive, press enter to skip): ")
            manager.update_camera(camera_id, location or None, status or None)
        elif choice == '3':
            camera_id = input("Enter camera ID: ")
            manager.delete_camera(camera_id)
        elif choice == '4':
            manager.display_cameras()
        elif choice == '5':
            camera_id = input("Enter camera ID to monitor: ")
            manager.monitor_surveillance_cameras(camera_id)
        elif choice == '6':
            footage_id = input("Enter footage ID to review: ")
            manager.review_camera_footage(footage_id)
        elif choice == '7':
            footage_id = input("Enter footage ID: ")
            camera_id = input("Enter camera ID related to the footage: ")
            timestamp = input("Enter timestamp of the footage: ")
            data = input("Enter data or description of the footage: ")
            manager.add_footage(footage_id, camera_id, timestamp, data)
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
